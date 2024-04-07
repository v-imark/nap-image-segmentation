<script lang="ts">
	import type { MetadataObject } from '../../types'
	import { Label } from './ui/label'
	import * as Tooltip from '$lib/components/ui/tooltip'
	import { IMAGE_NAMES, getPercentage } from '../../api'
	import { dataset, hovered_bar, selected_name } from '../../stores'
	let colors = ['bg-red-400', 'bg-amber-400', 'bg-emerald-500']
	let titles = ['min-area filter', 'IoU filter']

	export let data: MetadataObject
	let seg_info = data.segmentation_info

	$: masksRemoved = {
		after_min_area_filter: seg_info.after_sam - seg_info.after_min_area_filter,
		after_iou_filter: seg_info.after_min_area_filter - seg_info.after_iou_filter
	}

	export let width: number = 100
	export let height: number = 200
</script>

<div class="group w-[{width}px] pt-1">
	<div
		aria-hidden="true"
		class="flex w-[{width}px] flex-col justify-end rounded-t-md outline outline-0 hover:outline-2"
		style="height: {height}px; width: {width}px;"
		on:mouseenter={() => hovered_bar.set(data)}
	>
		{#each Object.entries(masksRemoved) as [key, val], index}
			<div
				class="w-full {colors[index]}"
				style="height: {getPercentage(val, seg_info.after_sam)}%;"
			/>
		{/each}

		<div class="w-full flex-auto {colors[2]}" />
	</div>
</div>
