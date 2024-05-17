export type Param = {
	id: string
	points_per_side: number
	pred_iou_thresh: number
	stability_score_thresh: number
	crop_n_layers: number
	crop_n_layers_downscale_factor: number
}

export type ParamSliderData = {
	sam_params: Omit<Param, 'id'>
	filters: {
		min_area: number
		iou_thresh: number
	}
}

export const ParamKeys = [
	'points_per_side',
	'pred_iou_thresh',
	'stability_score_thresh',
	'crop_n_layers',
	'crop_n_layers_downscale_factor'
] as (keyof ParamSliderData['sam_params'])[]

export const FilterKeys = ['min_area', 'iou_thresh'] as (keyof ParamSliderData['filters'])[]

export type Dataset = 'oxford_flowers102' | 'imagenet2012' | 'oxford_iiit_pet'

export type Mask = {
	name: string
	path: string
	area: number
	predicted_iou: number
	stability_score: number
	crop_box: number[]
	class_id: number
	ious: { name: string; iou: number }[]
}

export interface MetadataObject {
	name: string
	dataset: Dataset
	split: string
	params: {
		points_per_side: number
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
	masks: Mask[]
	annotated_image: string
}

export type Metadata = {
	[paramId: string]: MetadataObject
}

// type Colors = { [key: string]: string }
export const COLORS = ['ring-[#e41a1c]', 'ring-[#377eb8]', 'ring-[#4daf4a]']
export const BG_COLORS = ['bg-[#e41a1c]', 'bg-[#377eb8]', 'bg-[#4daf4a]', 'transparent']
export const BORDER_COLORS = ['border-[#e41a1c]', 'border-[#377eb8]', 'border-[#4daf4a]']

function indexOfMax(arr: number[]) {
	if (arr.length === 0) {
		return -1
	}

	let max = arr[0]
	let maxIndex = 0

	for (let i = 1; i < arr.length; i++) {
		if (arr[i] > max) {
			maxIndex = i
			max = arr[i]
		}
	}

	return maxIndex
}

export const getColor = (param: ParamSliderData, mask: Mask, masks: Mask[]) => {
	if (
		mask.predicted_iou < param.sam_params?.pred_iou_thresh ||
		mask.stability_score < param.sam_params?.stability_score_thresh
	) {
		return 4
	}
	const minArea = mask.crop_box[2] * mask.crop_box[3] * param.filters?.min_area
	if (mask.area < minArea) {
		return 0
	}
	if (mask.ious.length == 0) return 2
	const maxIou = mask.ious[indexOfMax(mask.ious.map((item) => item.iou))]
	const maxMask = masks.find((item) => item.name == maxIou.name) as Mask
	if (maxIou.iou > param.filters?.iou_thresh && mask.area < maxMask.area) {
		return 1
	}

	return 2
}

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
		title: 'Multi-config comparison',
		description:
			'This action cannot be undone. This will permanently delete your account and remove your datafrom our servers.'
	},
	{
		id: '/[run]/[param]/[dataset]/compare2',
		path: '/pps_test/pps-32/oxford_flowers102/compare2',
		title: 'Single-config comparison',
		description:
			'This action cannot be undone. This will permanently delete your account and remove your datafrom our servers.'
	},
	{
		id: '/[run]/overview',
		path: '/pps_test/overview',
		title: 'Dataset Overview',
		description:
			'This action cannot be undone. This will permanently delete your account and remove your datafrom our servers.'
	}
]

export const formatRouteParam = (param: string) => {
	return param.replace(/\]|\[/g, '')
}
