import { derived, writable } from 'svelte/store'
import { type Dataset, type MetadataObject } from './types'
import { filterAndAnnotate, getBarChartData } from './api'

export const selected_params = writable<string>('default')
export const dataset = writable<Dataset>('oxford_flowers102')
export const run = writable<string>('test2')
export const hovered_bar = writable<MetadataObject | undefined>()
export const min_area = writable<number>(0)
export const iou_threshold = writable<number>(1)
export const metaData = writable<MetadataObject>()
export const toggleTable = writable(false)

export const updateMetaData = async (
	min_area: number,
	iou_threshold: number,
	metadatas: MetadataObject[],
	img: string
) => {
	const metadata = metadatas.find((imgData) => imgData.name == img.split('.')[0]) as MetadataObject
	const data = await filterAndAnnotate(min_area, iou_threshold, metadata, img).then((val) => val)
	metaData.set(data)
	return data
}

export const barData = derived([selected_params, run], async ([$selected_params, $run]) => {
	const data = await getBarChartData($selected_params, $run)
	return data
})
