import { derived, writable } from 'svelte/store'
import { type Dataset } from './types'
import { IMAGE_NAMES, getAllMetaDataForImage, getMetaData } from './api'

export const selected_params = writable<string>('default')
export const dataset = writable<Dataset>('oxford_flowers102')
export const selected_name = writable<string>(IMAGE_NAMES['oxford_flowers102'][0])

export const data = derived(
	[selected_params, dataset, selected_name],
	async ([$selected_params, $dataset, $selected_name]) => {
		const data = await getMetaData($selected_params, $selected_name, $dataset).then((val) => val)
		return data
	}
)

export const all_data = derived([selected_name, dataset], async ([$selected_name, $dataset]) => {
	return await getAllMetaDataForImage($selected_name, $dataset)
})
