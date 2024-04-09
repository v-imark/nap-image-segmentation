<script lang="ts">
	import { getPercentage, getRelativePath } from '../../api'
	import type { MetadataObject } from '../../types'
	import { Label } from './ui/label'
	export let bar: MetadataObject

	$: masksRemoved = {
		after_min_area_filter:
			bar.segmentation_info.after_sam - bar.segmentation_info.after_min_area_filter,
		after_iou_filter:
			bar.segmentation_info.after_min_area_filter - bar.segmentation_info.after_iou_filter
	}

	$: src = getRelativePath(bar.annotated_image)
</script>

<div class="flex h-full w-64 flex-col space-y-1">
	<div class="h-44 w-full">
		<img
			src={`${src}?${masksRemoved.after_iou_filter}`}
			alt={bar.name}
			class="h-44 w-full object-scale-down"
		/>
	</div>
	<Label class="text-base">{bar.name}</Label>
	<Label>Initial masks: {bar.segmentation_info.after_sam}</Label>
	<Label>
		Removed by min-area filter: {masksRemoved.after_min_area_filter} ({getPercentage(
			masksRemoved.after_min_area_filter,
			bar.segmentation_info.after_sam,
			2
		)}%)
	</Label>
	<Label>
		Removed by IoU filter: {masksRemoved.after_iou_filter} ({getPercentage(
			masksRemoved.after_iou_filter,
			bar.segmentation_info.after_sam,
			2
		)}%)
	</Label>
	<Label>
		Final masks: {bar.segmentation_info.after_iou_filter} ({getPercentage(
			bar.segmentation_info.after_iou_filter,
			bar.segmentation_info.after_sam,
			2
		)}%)
	</Label>
</div>
