import type { Dataset, Metadata, MetadataObject, Param } from './types'

export const loadParams = async (): Promise<Param[]> => {
	const response = await fetch('http://localhost:5173/test_params.json')

	return response.json()
}

export const EXAMPLE_PARAMS: Param[] = await loadParams()
export const PARAM_IDS = EXAMPLE_PARAMS.map((val) => val.id)

export const IMAGE_NAMES = {
	oxford_flowers102: ['image_00001.jpg', 'image_00002.jpg', 'image_00003.jpg', 'image_00004.jpg'],
	imagenet2012: [
		'ILSVRC2012_test_00000001.JPEG',
		'ILSVRC2012_test_00000002.JPEG',
		'ILSVRC2012_test_00000003.JPEG',
		'ILSVRC2012_test_00000004.JPEG'
	]
}

export function getImageUrl(name: string, dataset: Dataset) {
	return `/data/images/${dataset}/test/${name}`
}

const getMetaDataUrl = (paramId: string, dataset: string) => {
	const param = EXAMPLE_PARAMS.find((val) => val.id == paramId) as Param
	const shorts = ['pps', 'ppb', 'pit', 'sst', 'cnl', 'cnldf', 'ma']
	let datasetFolder = `${dataset}`
	Object.entries(param).forEach(([, entry], index) => {
		if (index != 0) {
			datasetFolder += `_${shorts[index - 1]}-${entry}`
		}
	})

	return `/data/${paramId}/${datasetFolder}${param.min_area == 0 ? '.0' : ''}`
}

export const getMetaData = async (paramId: string, name: string, dataset: string) => {
	const url = getMetaDataUrl(paramId, dataset)
	const json: MetadataObject[] = await fetch(`${url}/metadata.json`).then((res) => {
		return res.json()
	})
	const img_name = name.split('.')[0]
	const data = json.find((val) => val.name == img_name) as MetadataObject
	return data
}

export const getAllMetaDataForImage = async (name: string, dataset: string) => {
	const metadata: Metadata = {}
	for (const id of PARAM_IDS) {
		metadata[id] = await getMetaData(id, name, dataset)
	}
	return metadata
}

export const getRelativePath = (path: string) => {
	const result = path.replace('\\', '/')
	return result.replace('frontend/static', '')
}
