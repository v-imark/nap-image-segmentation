import { derived, writable } from 'svelte/store'
import { type BarSorting, type Dataset, type MetadataObject, type Sorting } from './types'
import { IMAGE_NAMES, filterAndAnnotate, filterAndAnnotateAll, getBarChartData } from './api'

export const selected_params = writable<string>('default')
export const dataset = writable<Dataset>('oxford_flowers102')
export const run = writable<string>('test2')
export const hovered_bar = writable<MetadataObject | undefined>()
export const min_area = writable<number>(0)
export const iou_threshold = writable<number>(1)
export const metaData = writable<MetadataObject>()
export const toggleTable = writable(false)
export const toggleBars = writable(false)
export const sorting = writable<Sorting>('None')
export const barSorting = writable<BarSorting>('None')
export const ascending = writable(false)
export const toggleProbabilityView = writable(false)

export const updateMetaData = async (
	min_area: number,
	iou_threshold: number,
	metadatas: MetadataObject[],
	img: string
) => {
	const metadata = metadatas.find((imgData) => imgData.name == img.split('.')[0]) as MetadataObject
	const data: MetadataObject = await filterAndAnnotate(min_area, iou_threshold, metadata, img).then(
		(val) => val
	)
	return data
}

export const updateAllMetaData = async (
	min_area: number,
	iou_threshold: number,
	metadatas: MetadataObject[],
	dataset: Dataset
) => {
	const suffix = IMAGE_NAMES[dataset][0].split('.')[1]
	console.log(suffix)
	const newMetadatas: MetadataObject[] = await filterAndAnnotateAll(
		min_area,
		iou_threshold,
		metadatas,
		suffix
	).then((val) => val)

	return newMetadatas
}

export const barData = derived([selected_params, run], async ([$selected_params, $run]) => {
	const data = await getBarChartData($selected_params, $run)
	return data
})
