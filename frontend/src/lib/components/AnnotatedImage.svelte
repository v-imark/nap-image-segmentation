<script lang="ts">
	import { getImageUrl, getRelativePath, sortMasks } from '../../api'
	import { ascending, displayOptions, hoveredMask, run, sorting } from '../../stores'
	import { BG_COLORS, type MetadataObject } from '../../types'

	export let data: MetadataObject
	export let size = 800

	$: selected = sortMasks(data, $sorting, $ascending)
	const getSize = (w: number, h: number) => {
		if (h > w) {
			const newW = (size / h) * w
			return { w: Math.floor(newW), h: size }
		}
		const newH = (size / w) * h
		return { w: size, h: Math.floor(newH) }
	}

	$: sizes = getSize(selected.masks[0].crop_box[2], selected.masks[0].crop_box[3])
	$: console.log(sizes)
	$: src = getImageUrl(selected.name, selected.dataset, $run, true)
</script>

<div style="width: {sizes.w}px; height: {sizes.h}px;">
	<div class="relative mix-blend-multiply" style="width: {sizes.w}px; height: {sizes.h}px;">
		<img
			{src}
			alt={selected.name}
			class="absolute"
			style="width: {sizes.w}px; height: {sizes.h}px;"
		/>
		{#each selected.masks as mask}
			<div
				class="absolute h-full w-full opacity-60 {!$displayOptions[mask.class_id] &&
					'invisible'} {mask.name == $hoveredMask
					? 'z-50 bg-yellow-400'
					: BG_COLORS[mask.class_id]}"
				style="
                    mask-image: url({getRelativePath(mask.path)}/{mask.name});
                    mask-size: 100% 100%;
                    "
			></div>
		{/each}
	</div>
</div>
