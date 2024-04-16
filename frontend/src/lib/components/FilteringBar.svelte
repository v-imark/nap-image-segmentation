<script lang="ts">
	import { getPercentage } from '../../api'
	import { displayOptions } from '../../stores'
	import { BG_COLORS, type MetadataObject } from '../../types'
	let colors = ['bg-red-400', 'bg-amber-400', 'bg-emerald-500']
	let titles = ['min-area filter', 'IoU filter']

	export let data: MetadataObject
	$: seg_info = data.segmentation_info

	$: masksRemoved = {
		after_min_area_filter: seg_info.after_sam - seg_info.after_min_area_filter,
		after_iou_filter: seg_info.after_min_area_filter - seg_info.after_iou_filter
	}

	export let width: number = 100
	export let height: number = 200
	export let h_bar: MetadataObject
</script>

<div class="group w-[{width}px] flex h-full items-end">
	<div
		aria-hidden="true"
		class="flex w-[{width}px] flex-col justify-end rounded-t-md outline outline-0 hover:outline-2"
		style="height: {height}px; width: {width}px;"
		on:mouseenter={() => (h_bar = data)}
	>
		{#each Object.entries(masksRemoved) as [key, val], index}
			{#if val != 0}
				<div
					class="w-full {BG_COLORS[index]} first:rounded-t-md {!$displayOptions[index] && 'hidden'}"
					style="height: {getPercentage(val, seg_info.after_sam)}%;"
				/>
			{/if}
		{/each}
		<div
			class="w-full flex-auto {BG_COLORS[2]} first:rounded-t-md {!$displayOptions[2] && 'hidden'}"
		/>
	</div>
</div>
