export interface Param {
	id: string
	points_per_side: number
	points_per_batch: number
	pred_iou_thresh: number
	stability_score_thresh: number
	crop_n_layers: number
	crop_n_layers_downscale_factor: number
	min_area: number
}

export type Dataset = 'oxford_flowers102' | 'imagenet2012'

export interface MetadataObject {
	name: string
	dataset: string
	split: string
	params: {
		points_per_side: number
		points_per_batch: number
		pred_iou_thresh: number
		stability_score_thresh: number
		crop_n_layers: number
		crop_n_layers_downscale_factor: number
		min_area: number
	}
	segmentation_info: {
		initial_size: number
		final_size: number
	}
	masks: {
		name: string
		path: string
		area: number
		predicted_iou: number
		stability_score: number
		crop_box: number[]
	}[]
	annotated_image: string
}

export type Metadata = {
	[paramId: string]: MetadataObject
}
