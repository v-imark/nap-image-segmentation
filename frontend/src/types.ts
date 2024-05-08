export interface Param {
	id: string
	points_per_side: number
	pred_iou_thresh: number
	stability_score_thresh: number
	crop_n_layers: number
	crop_n_layers_downscale_factor: number
}

export type Dataset = 'oxford_flowers102' | 'imagenet2012' | 'oxford_iiit_pet'

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
		ious: { name: string; iou: number }
	}[]
	annotated_image: string
}

export type Metadata = {
	[paramId: string]: MetadataObject
}

// type Colors = { [key: string]: string }
export const COLORS = ['ring-[#e41a1c]', 'ring-[#377eb8]', 'ring-[#4daf4a]']
export const BG_COLORS = ['bg-[#e41a1c]', 'bg-[#377eb8]', 'bg-[#4daf4a]']

export type Sorting = 'None' | 'area' | 'stability_score' | 'predicted_iou' | 'class_id'
export type BarSorting =
	| 'None'
	| 'after_sam'
	| 'after_min_area_filter'
	| 'after_iou_filter'
	| 'removed_by_min_area'
	| 'removed_by_iou_thresh'

export type RouteInfo = { id: string; path: string; title: string; description: string }
export const ROUTES: RouteInfo[] = [
	{
		id: '/',
		path: '/',
		title: 'Home',
		description:
			'This action cannot be undone. This will permanently delete your account and remove your datafrom our servers.'
	},
	{
		id: '/[run]/[param]/[dataset]/compare',
		path: '/pps_test/pps-32/oxford_flowers102/compare',
		title: 'Compare Params',
		description:
			'This action cannot be undone. This will permanently delete your account and remove your datafrom our servers.'
	},
	{
		id: '/[run]/[param]/[dataset]/[dataset]/compare2',
		path: '/pps_test/pps-32/oxford_flowers102/compare2',
		title: 'Compare Params 2',
		description:
			'This action cannot be undone. This will permanently delete your account and remove your datafrom our servers.'
	},
	{
		id: '/[run]/overview',
		path: 'pps_test/overview',
		title: 'Dataset Overview',
		description:
			'This action cannot be undone. This will permanently delete your account and remove your datafrom our servers.'
	}
]

export const formatRouteParam = (param: string) => {
	return param.replace(/\]|\[/g, '')
}
