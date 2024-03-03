import Papa from 'papaparse'
import { writable, type Writable } from 'svelte/store'

export const points_per_side = writable<number>(32)
export const points_per_batch = writable(64)
export const pred_iou_thresh = writable(0.88)
export const stability_score_thresh = writable(0.95)
export const crop_n_layers = writable(0)
export const crop_n_layers_downscale_factor = writable(1)
export const min_area = writable(0.01)

type SegmentationParam = {
	default: number
	min: number
	max: number
	step: number
	writable: Writable<number>
}

export const SEGMENTATION_PARAMS: { [key: string]: SegmentationParam } = {
	points_per_side: {
		default: 32,
		min: 1,
		max: 100,
		step: 1,
		writable: points_per_side
	},
	points_per_batch: {
		default: 64,
		min: 32,
		max: 128,
		step: 1,
		writable: points_per_batch
	},
	pred_iou_thresh: {
		default: 0.88,
		min: 0.0,
		max: 1.0,
		step: 0.01,
		writable: pred_iou_thresh
	},
	stability_score_thresh: {
		default: 0.95,
		min: 0.0,
		max: 1.0,
		step: 0.01,
		writable: stability_score_thresh
	},
	crop_n_layers: {
		default: 0,
		min: 0,
		max: 5,
		step: 1,
		writable: crop_n_layers
	},
	crop_n_layers_downscale_factor: {
		default: 1,
		min: 1,
		max: 5,
		step: 1,
		writable: crop_n_layers_downscale_factor
	},
	min_area: {
		default: 0.01,
		min: 0.0,
		max: 1.0,
		step: 0.01,
		writable: min_area
	}
}

export const resetStore = () => {
	Object.entries(SEGMENTATION_PARAMS).forEach(([, param]) => param.writable.set(param.default))
}

export const dataset = writable()

export type Param = {
	[key: string]: number
}

export interface SegParams {
	[id: string]: Param
}

export const EXAMPLE_PARAMS: SegParams = {
	param1: {
		points_per_side: 32,
		points_per_batch: 64,
		pred_iou_thresh: 0.88,
		stability_score_thresh: 0.95,
		crop_n_layers: 0,
		crop_n_layers_downscale_factor: 1,
		min_area: 0.01
	},
	param2: {
		points_per_side: 32,
		points_per_batch: 64,
		pred_iou_thresh: 0.88,
		stability_score_thresh: 0.95,
		crop_n_layers: 0,
		crop_n_layers_downscale_factor: 1,
		min_area: 0.01
	}
}
export const PARAMS = Papa.parse('', {
	complete: function (results) {
		console.log(results)
		return results
	}
})
export const SEG_PARAMS = Object.entries(EXAMPLE_PARAMS)
export const PARAM_IDS = Object.keys(EXAMPLE_PARAMS)

export const selected_params = writable<string[]>(PARAM_IDS)
