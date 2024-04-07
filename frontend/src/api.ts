//import { metaData } from './stores'
import type { Dataset, Metadata, MetadataObject, Param } from './types'

export const loadParams = async (): Promise<{ [key: string]: Param[] }> => {
	const response = await fetch('http://localhost:5173/test_params.json')

	return response.json()
}

export const EXAMPLE_PARAMS: { [key: string]: Param[] } = await loadParams()
export const PARAM_IDS = (run: string) => EXAMPLE_PARAMS[run].map((val) => val.id)

export const getImageNames = async () => {
	const imagenet: string[] = await fetch(
		'http://localhost:5173/data/test2/images/imagenet2012/image_names.json'
	).then((val) => val.json())
	const oxford: string[] = await fetch(
		'http://localhost:5173/data/test2/images/oxford_flowers102/image_names.json'
	).then((val) => val.json())

	return {
		imagenet2012: imagenet,
		oxford_flowers102: oxford
	}
}

export const IMAGE_NAMES = await getImageNames()

export function getImageUrl(name: string, dataset: Dataset, run: string, search?: boolean) {
	if (search) {
		const imgName = IMAGE_NAMES[dataset].find((value) => value.split('.')[0] == name)
		return `/data/${run}/images/${dataset}/test/${imgName}`
	}

	return `/data/${run}/images/${dataset}/test/${name}`
}

const getMetaDataUrl = (paramId: string, dataset: string, run: string) => {
	const param = EXAMPLE_PARAMS[run].find((val) => val.id == paramId) as Param
	const shorts = ['pps', 'ppb', 'pit', 'sst', 'cnl', 'cnldf']
	let datasetFolder = `${dataset}`
	Object.entries(param).forEach(([, entry], index) => {
		if (index != 0 && index - 1 < shorts.length) {
			datasetFolder += `_${shorts[index - 1]}-${entry}`
		}
	})
	const ma = param.min_area == 0 ? `ma-${param.min_area}.0` : `ma-${param.min_area}`
	const it = param.iou_thresh == 1 ? `it-${param.iou_thresh}.0` : `it-${param.iou_thresh}`
	return `/data/${run}/${paramId}/${datasetFolder}_${ma}_${it}`
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

export const getAllMetaDataForImage = async (name: string, dataset: string, run: string) => {
	const metadata: Metadata = {}
	for (const id of PARAM_IDS(run)) {
		metadata[id] = await getMetaData(id, name, dataset, run)
	}
	return metadata
}

export const getRelativePath = (path: string) => {
	const result = path.replace('\\', '/')
	return result.replace('frontend/static', '')
}

export const getBarChartData = async (paramId: string, run: string) => {
	const url = getMetaDataUrl(paramId, 'imagenet2012', run)
	const imagenet_json: MetadataObject[] = await fetch(`${url}/metadata.json`).then((res) => {
		return res.json()
	})
	const url2 = getMetaDataUrl(paramId, 'oxford_flowers102', run)
	const oxford_json: MetadataObject[] = await fetch(`${url2}/metadata.json`).then((res) => {
		return res.json()
	})

	return { imagenet2012: imagenet_json, oxford_flowers102: oxford_json }
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
