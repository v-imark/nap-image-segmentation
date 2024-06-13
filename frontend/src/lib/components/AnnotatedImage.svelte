<script lang="ts">
	import { getImageUrl, getRelativePath, sortMasks } from '../../api'
	import { ascending, displayOptions, sorting, colorMap, strategy, strategyKey } from '../../stores'
	import {
		BG_COLORS,
		getBgColor,
		getFilterClass,
		type MetadataObject,
		type ParamSliderData
	} from '../../types'

	export let data: MetadataObject
	export let params: ParamSliderData
	export let size = 800
	export let src = 'example'
	export let hovered: string = ''

	$: selected = sortMasks(data, $sorting, $ascending)
	const getSize = (w: number, h: number) => {
		if (h > w) {
			const newW = (size / h) * w
			return { w: Math.floor(newW), h: size, scale: size / h }
		}
		const newH = (size / w) * h
		return { w: size, h: Math.floor(newH), scale: size / w }
	}

	$: sizes = getSize(selected?.masks[0].crop_box[2], selected?.masks[0].crop_box[3])
	const getOutlineSize = (bbox: number[]) => {
		const x = Math.round(bbox[0] * sizes.scale)
		const y = Math.round(bbox[1] * sizes.scale)
		const w = Math.round(bbox[2] * sizes.scale)
		const h = Math.round(bbox[3] * sizes.scale)
		return { x, y, w, h }
	}
</script>

{#if selected}
	<div style="width: {sizes.w}px; height: {sizes.h}px;">
		<div class="relative" style="width: {sizes.w}px; height: {sizes.h}px;">
			<img
				{src}
				alt={selected?.name}
				class="absolute"
				style="width: {sizes.w}px; height: {sizes.h}px;"
			/>
			{#each selected.masks as mask, i}
				{@const class_id = getFilterClass(params, mask, selected.masks)}
				{@const color = getBgColor(
					$colorMap,
					$strategy,
					params,
					mask,
					selected.masks,
					i,
					$strategyKey.value
				)}
				{@const outline = getOutlineSize(mask.bbox)}
				<div
					class="absolute h-full w-full opacity-60
					{mask.name == hovered ? 'z-50 bg-fuchsia-400' : color}
						{(class_id == 4 || !$displayOptions[class_id]) && 'invisible'}"
					style="
                    mask-image: url({getRelativePath(mask.path)}/{mask.name});
                    mask-size: 100% 100%;
                    "
				></div>
				{#if mask.name == hovered}
					<div
						class="absolute z-50 outline outline-fuchsia-400"
						style="width: {outline.w}px; height: {outline.h}px; top: {outline.y}px; left: {outline.x}px;"
					></div>
				{/if}
			{/each}
		</div>
	</div>
{/if}
