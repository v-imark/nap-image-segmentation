export interface Param {
	id: string
	points_per_side: number
	points_per_batch: number
	pred_iou_thresh: number
	stability_score_thresh: number
	crop_n_layers: number
	crop_n_layers_downscale_factor: number
	min_area: number
	iou_thresh: number
}

export type Dataset = 'oxford_flowers102' | 'imagenet2012'

export interface MetadataObject {
	name: string
	dataset: Dataset
	split: string
	params: {
		points_per_side: number
		points_per_batch: number
		pred_iou_thresh: number
		stability_score_thresh: number
		crop_n_layers: number
		crop_n_layers_downscale_factor: number
		min_area: number
		iou_thresh: number
	}
	segmentation_info: {
		after_sam: number
		after_min_area_filter: number
		after_iou_filter: number
	}
	masks: {
		name: string
		path: string
		area: number
		predicted_iou: number
		stability_score: number
		crop_box: number[]
		class_id: number
	}[]
	annotated_image: string
}

export type Metadata = {
	[paramId: string]: MetadataObject
}

// type Colors = { [key: string]: string }
export const COLORS = ['ring-[#e41a1c]', 'ring-[#377eb8]', 'ring-[#4daf4a]']
export const BG_COLORS = ['bg-[#e41a1c]', 'bg-[#377eb8]', 'bg-[#4daf4a]']
