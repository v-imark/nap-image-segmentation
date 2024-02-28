import type { Writable } from 'svelte/store'
import {
	crop_n_layers,
	crop_n_layers_downscale_factor,
	min_area,
	points_per_batch,
	points_per_side,
	pred_iou_thresh,
	stability_score_thresh
} from './stores'

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
