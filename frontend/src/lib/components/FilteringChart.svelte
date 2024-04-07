<script lang="ts">
	import { getImageUrl, getPercentage } from '../../api'
	import { hovered_bar, run } from '../../stores'
	import type { MetadataObject } from '../../types'
	import FilteringBar from './FilteringBar.svelte'
	import { Label } from './ui/label'

	export let data: MetadataObject[]

	const max = Math.max(...data.map((val) => val.segmentation_info.after_sam))
</script>

<div class="flex w-full flex-row items-end space-x-1 pl-0.5">
	{#each data as item}
		<FilteringBar data={item} height={(item.segmentation_info.after_sam / max) * 300} width={10} />
	{/each}
	{#if $hovered_bar}
		{@const masksRemoved = {
			after_min_area_filter:
				$hovered_bar.segmentation_info.after_sam -
				$hovered_bar.segmentation_info.after_min_area_filter,
			after_iou_filter:
				$hovered_bar.segmentation_info.after_min_area_filter -
				$hovered_bar.segmentation_info.after_iou_filter
		}}
		{@const src = getImageUrl($hovered_bar.name, $hovered_bar.dataset, $run, true)}
		<div class="flex h-full flex-col space-y-1">
			<div class="h-48 w-full">
				<img {src} alt={$hovered_bar.name} class="h-48 w-full object-scale-down" />
			</div>

			<Label class="text-base">{$hovered_bar.name}</Label>
			<Label>Initial masks: {$hovered_bar.segmentation_info.after_sam}</Label>
			<Label>
				Removed by min-area filter: {masksRemoved.after_min_area_filter} ({getPercentage(
					masksRemoved.after_min_area_filter,
					$hovered_bar.segmentation_info.after_sam,
					2
				)}%)
			</Label>
			<Label>
				Removed by IoU filter: {masksRemoved.after_iou_filter} ({getPercentage(
					masksRemoved.after_iou_filter,
					$hovered_bar.segmentation_info.after_sam,
					2
				)}%)
			</Label>
			<Label>
				Final masks: {$hovered_bar.segmentation_info.after_iou_filter} ({getPercentage(
					$hovered_bar.segmentation_info.after_iou_filter,
					$hovered_bar.segmentation_info.after_sam,
					2
				)}%)
			</Label>
		</div>
	{/if}
</div>
