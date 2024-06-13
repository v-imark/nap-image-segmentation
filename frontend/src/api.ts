//import { metaData } from './stores'
import type { BarSorting, Dataset, MetadataObject, Param, Sorting } from './types'

export const loadParams = async (): Promise<{ [key: string]: Param[] }> => {
	const response = await fetch('http://localhost:5173/test_params.json')

	return response.json()
}

export const EXAMPLE_PARAMS: { [key: string]: Param[] } = await loadParams()
// export const PARAM_IDS = (run: string) => EXAMPLE_PARAMS[run].map((val) => val.id)

export const getImageNames = async () => {
	const imagenet: string[] = await fetch(
		'http://localhost:5173/data/pps_test/images/imagenet2012/image_names.json'
	).then((val) => val.json())
	const oxford: string[] = await fetch(
		'http://localhost:5173/data/pps_test/images/oxford_flowers102/image_names.json'
	).then((val) => val.json())
	const oxford_pets: string[] = await fetch(
		'http://localhost:5173/data/pps_test/images/oxford_iiit_pet/image_names.json'
	).then((val) => val.json())

	return {
		imagenet2012: imagenet,
		oxford_flowers102: oxford,
		oxford_iiit_pet: oxford_pets
	}
}

// export const IMAGE_NAMES = await getImageNames()

export function getImageUrl(
	name: string,
	dataset: Dataset,
	run: string,
	imageNames: string[],
	search?: boolean
) {
	if (search) {
		const imgName = imageNames.find((value) => value.split('.')[0] == name)
		return `/data/${run}/images/${dataset}/test/${imgName}`
	}

	return `/data/${run}/images/${dataset}/test/${name}`
}

export const getMetaDataUrl = (paramId: string, dataset: string, run: string) => {
	const param = EXAMPLE_PARAMS[run].find((val) => val.id == paramId) as Param
	const shorts = ['pps', 'pit', 'sst', 'cnl', 'cnldf']
	let datasetFolder = `${dataset}`
	Object.entries(param).forEach(([, entry], index) => {
		if (index != 0) {
			datasetFolder += `_${shorts[index - 1]}-${entry}`
		}
	})
	return `/data/${run}/${paramId}/${datasetFolder}`
}

export const getMetaData = async (paramId: string, name: string, dataset: string, run: string) => {
	const url = getMetaDataUrl(paramId, dataset, run)
	const json: MetadataObject[] = await fetch(`${url}/metadata.json`).then((res) => {
		return res.json()
	})
	const img_name = name.split('.')[0]
	const data = json.find((val) => val.name == img_name) as MetadataObject
	return data
}

// export const getAllMetaDataForImage = async (name: string, dataset: string, run: string) => {
// 	const metadata: Metadata = {}
// 	for (const id of PARAM_IDS(run)) {
// 		metadata[id] = await getMetaData(id, name, dataset, run)
// 	}
// 	return metadata
// }

export const getRelativePath = (path: string) => {
	const result = path.toString().replace(/\\/g, '/')
	return result.replace('frontend/static', '')
}

export const makeBgsTransparent = async (metadata: MetadataObject) => {
	const result = await fetch('http://127.0.0.1:5000/api/transparent', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			query: { masks: metadata.masks }
		})
	}).then((res) => res.json())
	return result
}

export const getBarChartData = async (paramId: string, run: string) => {
	const url = getMetaDataUrl(paramId, 'imagenet2012', run)
	const imagenet_json: MetadataObject[] = await fetch(`${url}/metadata.json`).then((res) => {
		return res.status != 404 ? res.json() : []
	})
	const url2 = getMetaDataUrl(paramId, 'oxford_flowers102', run)
	const oxford_json: MetadataObject[] = await fetch(`${url2}/metadata.json`).then((res) => {
		return res.status != 404 ? res.json() : []
	})
	const url3 = getMetaDataUrl(paramId, 'oxford_iiit_pet', run)
	const oxford_pets_json: MetadataObject[] = await fetch(`${url3}/metadata.json`).then((res) => {
		return res.status != 404 ? res.json() : []
	})

	return {
		imagenet2012: imagenet_json,
		oxford_flowers102: oxford_json,
		oxford_iiit_pet: oxford_pets_json
	}
}

export const formatBarDataForDataset = (data: MetadataObject[]) => {
	const after_sam = data
		.map((val) => val.segmentation_info.after_sam)
		.reduce((sum, current) => sum + current)
	const after_min_area_filter = data
		.map((val) => val.segmentation_info.after_min_area_filter)
		.reduce((sum, current) => sum + current)
	const after_iou_filter = data
		.map((val) => val.segmentation_info.after_iou_filter)
		.reduce((sum, current) => sum + current)

	return {
		after_sam: after_sam,
		after_min_area_filter: after_min_area_filter,
		after_iou_filter: after_iou_filter
	}
}

export const formatBarData = (data: {
	imagenet2012: MetadataObject[]
	oxford_flowers102: MetadataObject[]
}) => {
	const imagenet = formatBarDataForDataset(data.imagenet2012)
	const oxford = formatBarDataForDataset(data.oxford_flowers102)

	return {
		after_sam: imagenet.after_sam + oxford.after_sam,
		after_min_area_filter: imagenet.after_min_area_filter + oxford.after_min_area_filter,
		after_iou_filter: imagenet.after_iou_filter + oxford.after_iou_filter
	}
}

export const getSpanForDataset = (
	data: MetadataObject[],
	param: 'after_min_area_filter' | 'after_iou_filter'
) => {
	const comparator = param == 'after_min_area_filter' ? 'after_sam' : 'after_min_area_filter'

	const max = Math.max(
		...data.map((val) => val.segmentation_info[param] / val.segmentation_info[comparator])
	)
	const min = Math.min(
		...data.map((val) => val.segmentation_info[param] / val.segmentation_info[comparator])
	)

	return { min, max }
}

export const getSpan = (
	data: {
		imagenet2012: MetadataObject[]
		oxford_flowers102: MetadataObject[]
	},
	param: 'after_min_area_filter' | 'after_iou_filter'
) => {
	const max = Math.max(
		getSpanForDataset(data.imagenet2012, param).max,
		getSpanForDataset(data.oxford_flowers102, param).max
	)
	const min = Math.min(
		getSpanForDataset(data.imagenet2012, param).min,
		getSpanForDataset(data.oxford_flowers102, param).min
	)

	return { min, max }
}

export const getPercentage = (value: number, of: number, decimals: number = 5) => {
	return ((value / of) * 100).toFixed(decimals)
}

export const filterAndAnnotate = async (
	min_area: number,
	threshold: number,
	metadata: MetadataObject,
	img: string
) => {
	const data = await fetch('http://127.0.0.1:5000/api/filter', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			query: { metadata: metadata, min_area: min_area, threshold: threshold, img: img }
		})
	}).then((res) => res.json())
	return JSON.parse(data)
}

export const filterAndAnnotateAll = async (
	min_area: number,
	threshold: number,
	metadata: MetadataObject[],
	suffix: string
) => {
	const data = await fetch('http://127.0.0.1:5000/api/filter_all', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			query: { metadata: metadata, min_area: min_area, threshold: threshold, suffix: suffix }
		})
	}).then((res) => res.json())
	return JSON.parse(data)
}

export const sortMasks = (data: MetadataObject, key: Sorting, ascending: boolean) => {
	if (key == 'None') return data
	const sorted = data
	sorted.masks = sorted.masks.sort((a, b) => (ascending ? a[key] - b[key] : b[key] - a[key]))
	return sorted
}

export const sortBars = (data: MetadataObject[], key: BarSorting, ascending: boolean) => {
	if (key == 'None') return data
	if (key == 'removed_by_min_area') {
		const sorted = data.sort((a, b) => {
			const a_removed = a.segmentation_info.after_sam - a.segmentation_info.after_min_area_filter
			const b_removed = b.segmentation_info.after_sam - b.segmentation_info.after_min_area_filter
			return ascending ? a_removed - b_removed : b_removed - a_removed
		})
		return sorted
	}
	if (key == 'removed_by_iou_thresh') {
		const sorted = data.sort((a, b) => {
			const a_removed =
				a.segmentation_info.after_min_area_filter - a.segmentation_info.after_iou_filter
			const b_removed =
				b.segmentation_info.after_min_area_filter - b.segmentation_info.after_iou_filter
			return ascending ? a_removed - b_removed : b_removed - a_removed
		})
		return sorted
	}

	return data.sort((a, b) =>
		ascending
			? a.segmentation_info[key] - b.segmentation_info[key]
			: b.segmentation_info[key] - a.segmentation_info[key]
	)
}

export const getRoute = (
	runs: string[],
	params: string[],
	dataset: string,
	current: string | null
) => {
	if (params.length > 1) {
		return current
			?.replace('[runLeftxrunRight]', `${runs[0]}x${runs[1]}`)
			.replace('[paramLeftxparamRight]', `${params[0]}x${params[1]}`)
			.replace('[dataset]', dataset)
	}

	return current
		?.replace('[run]', runs[0])
		.replace('[param]', params[0])
		.replace('[dataset]', dataset)
}
