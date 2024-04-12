<script lang="ts">
	import { onMount } from 'svelte'
	import type { MetadataObject } from '../../types'
	import { IMAGE_NAMES, getImageUrl, getRelativePath, makeBgsTransparent } from '../../api'
	import { dataset, run } from '../../stores'
	import * as Select from './ui/select'
	import MaskTable from './MaskTable.svelte'
	import { Separator } from './ui/separator'

	export let data: MetadataObject[]
	let selected = data[0]
	let hovered = ''
	let loading = true
	let key = 0
	onMount(async () => {
		await makeBgsTransparent(selected)
		loading = false
	})
	$: src = getImageUrl(selected.name, selected.dataset, $run, true)

	const size = 800

	const getSize = (w: number, h: number) => {
		if (h > w) {
			const newW = (size / h) * w
			return { w: Math.round(newW), h: size }
		}
		const newH = (size / w) * h
		return { w: size, h: Math.round(newH) }
	}
</script>

<div class="flex h-full flex-col space-y-3">
	<Select.Root
		selected={{ value: selected }}
		onSelectedChange={async (val) => {
			loading = true
			await makeBgsTransparent(val?.value ?? selected)
			selected = val?.value ?? selected
			loading = false
			key++
		}}
	>
		<Select.Trigger class="w-[280px]">
			<Select.Value placeholder="Select image" />
		</Select.Trigger>
		<Select.Content class="h-[600px] overflow-y-auto">
			{#each data as item}
				<Select.Item value={item}>{item.name}</Select.Item>
			{/each}
		</Select.Content>
	</Select.Root>
	<Separator />
	<div class="flex w-full space-x-3">
		{#if !loading}
			{@const sizes = getSize(selected.masks[0].crop_box[2], selected.masks[0].crop_box[3])}
			<div style="width: {size}px; height: {sizes.h}px;">
				<div class="relative mix-blend-multiply" style="width: {sizes.w}px; height: {sizes.h}px;">
					<img
						{src}
						alt={selected.name}
						class="absolute"
						style="width: {sizes.w}px; height: {sizes.h}px;"
					/>
					{#each selected.masks as mask}
						<div
							class="absolute opacity-50 {mask.name == hovered ? 'bg-yellow-400' : 'bg-red-700'}"
							style="
								width: {sizes.w}px;
								height: {sizes.h}px;
								mask-image: url({getRelativePath(mask.path)}/{mask.name});
								mask-size: contain;
								"
						></div>
					{/each}
				</div>
			</div>
			<div class="h-[864px] flex-auto">
				<MaskTable data={selected} probabilityView={true} bind:hovered />
			</div>
		{/if}
	</div>
</div>
