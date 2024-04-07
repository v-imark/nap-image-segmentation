<script lang="ts">
	import { IMAGE_NAMES, getImageUrl, getRelativePath } from '../../api'
	import { iou_threshold, min_area, run, updateMetaData } from '../../stores'
	import Slider from './ui/slider/slider.svelte'
	import { Label } from './ui/label'
	import { Separator } from './ui/separator'
	import { Switch } from './ui/switch'
	import * as Select from './ui/select'
	import type { Dataset, MetadataObject } from '../../types'

	export let dataset: Dataset
	export let data: MetadataObject[]
	export let selectedMetaData = data[0]

	let selectedName = {
		value: IMAGE_NAMES[dataset].find((value) => value.split('.')[0] == selectedMetaData.name) ?? ''
	}

	$: src = getImageUrl(selectedName.value, dataset, $run)
	$: anno_src = getRelativePath(selectedMetaData ? selectedMetaData.annotated_image : '')
	$: min_area_val = [0]
	$: iou_threshold_val = [1]
	$: key = 0
	let annotate = true

	let loading = false
</script>

<div class="flex h-full w-full items-center justify-center space-x-3">
	{#if annotate}
		<img
			src={`${anno_src}?${key}`}
			alt={`${selectedMetaData.segmentation_info.after_sam}-${selectedMetaData.segmentation_info.after_min_area_filter}-${selectedMetaData.segmentation_info.after_iou_filter}`}
			class="z-50 h-56 object-scale-down hover:scale-150 {loading
				? 'animate-pulse'
				: 'animate-none'}"
		/>
	{:else}
		<img {src} alt={selectedName.value} class="h-56 hover:scale-150" />
	{/if}

	<div class="flex flex-col space-y-2">
		<Select.Root
			bind:selected={selectedName}
			onSelectedChange={async (val) => {
				loading = true
				selectedMetaData = await updateMetaData(
					min_area_val[0],
					iou_threshold_val[0],
					data,
					val?.value ?? selectedName.value
				)
				key += 1
				loading = false
			}}
		>
			<Select.Trigger class="w-[280px]">
				<Select.Value placeholder="Select image" />
			</Select.Trigger>
			<Select.Content class="h-[600px] overflow-y-auto">
				{#each IMAGE_NAMES[dataset] as imgName}
					<Select.Item value={imgName}>{imgName}</Select.Item>
				{/each}
			</Select.Content>
		</Select.Root>
		<div class="flex items-center space-x-2">
			<Switch id="annotate-image" bind:checked={annotate} />
			<Label for="annotate-image">Annotate image</Label>
		</div>
		<Separator />
		<div class="flex w-full flex-col items-center space-y-1">
			<Label>{min_area_val[0]}</Label>
			<Slider
				bind:value={min_area_val}
				onValueChange={async (value) => {
					min_area.set(value[0])
					loading = true
					selectedMetaData = await updateMetaData(
						value[0],
						iou_threshold_val[0],
						data,
						selectedName.value
					)
					key += 1
					loading = false
				}}
				min={0}
				max={1}
				step={0.01}
			></Slider>
			<Label>min_area</Label>
		</div>
		<Separator />
		<div class="flex w-full flex-col items-center space-y-1">
			<Label>{iou_threshold_val[0]}</Label>
			<Slider
				bind:value={iou_threshold_val}
				onValueChange={async (value) => {
					iou_threshold.set(value[0])
					loading = true
					selectedMetaData = await updateMetaData(
						min_area_val[0],
						value[0],
						data,
						selectedName.value
					)
					key += 1
					loading = false
				}}
				min={0}
				max={1}
				step={0.01}
			></Slider>
			<Label>iou_threshold</Label>
		</div>
	</div>
</div>
