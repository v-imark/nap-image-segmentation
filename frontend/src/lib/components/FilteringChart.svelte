<script lang="ts">
	import { sortBars } from '../../api'
	import { ascending, barSorting, updateAllMetaData } from '../../stores'
	import type { MetadataObject } from '../../types'
	import FilteringBar from './FilteringBar.svelte'
	import MasksInfo from './MasksInfo.svelte'
	import Button from './ui/button/button.svelte'
	import { Label } from './ui/label'
	import { Separator } from './ui/separator'
	import { Slider } from './ui/slider'

	export let data: MetadataObject[]

	const max = Math.max(...data.map((val) => val.segmentation_info.after_sam))
	const width = 700 / data.length
	let selectedMetaData = data
	$: min_area_val = [0]
	$: iou_threshold_val = [1]
	let disabled = false
	let h_bar: MetadataObject = selectedMetaData[0]
</script>

<div class="flex w-min flex-col space-y-2">
	<div class="flex flex-col">
		<div class="flex h-80 flex-row items-end space-x-1 px-0.5">
			<div class="flex h-full flex-col items-end justify-between">
				<Label>{max}</Label>
				<Label class="rotate-180 self-center" style="writing-mode: tb;">Number of masks</Label>
				<Label>0</Label>
			</div>
			<Separator orientation="vertical" class="w-[2px] bg-black" />
			{#each sortBars(selectedMetaData, $barSorting, $ascending) as item}
				<FilteringBar
					data={item}
					height={(item.segmentation_info.after_sam / max) * 320}
					{width}
					bind:h_bar
				/>
			{/each}
			{#if h_bar}
				<MasksInfo bar={h_bar} />
			{/if}
		</div>
		<div class="pl-3">
			<Separator class="h-[2px] bg-black " />
		</div>
		<Label class="self-center">Image</Label>
	</div>
	<Separator />
	<div class="flex w-full items-center space-x-2">
		<div class="flex w-full flex-col space-y-2">
			<div class="flex w-full flex-row items-center space-x-2 px-2">
				<Label class="w-28">min_area</Label>
				<Slider bind:value={min_area_val} min={0} max={0.5} step={0.005} {disabled}></Slider>
				<Label class="w-12 text-right">{min_area_val[0]}</Label>
			</div>
			<Separator />
			<div class="flex w-full flex-row items-center space-x-2 px-2">
				<Label class="w-28">iou_threshold</Label>
				<Slider bind:value={iou_threshold_val} min={0} max={1} step={0.01} {disabled}></Slider>
				<Label class="w-12 text-right">{iou_threshold_val[0]}</Label>
			</div>
		</div>
		<Separator orientation="vertical" />
		<Button
			class="w-28"
			{disabled}
			on:click={async () => {
				disabled = true
				selectedMetaData = await updateAllMetaData(
					min_area_val[0],
					iou_threshold_val[0],
					data,
					data[0].dataset
				)
				disabled = false
			}}
		>
			{disabled ? 'LOADING' : 'FILTER'}
		</Button>
	</div>
	<Separator />
</div>
