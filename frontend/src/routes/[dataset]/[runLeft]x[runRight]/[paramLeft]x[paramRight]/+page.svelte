<script lang="ts">
	import { navigating, page } from '$app/stores'
	import ColorInfo from '$lib/components/ColorInfo.svelte'
	import ColorMapSelect from '$lib/components/ColorMapSelect.svelte'
	import CompareColumn from '$lib/components/CompareColumn.svelte'
	import DisplayOptions from '$lib/components/DisplayOptions.svelte'
	import Header from '$lib/components/Header.svelte'
	import ImageSelector from '$lib/components/ImageSelector.svelte'
	import MainLayout from '$lib/components/MainLayout.svelte'
	import SortingSelect from '$lib/components/SortingSelect.svelte'
	import StrategySelect from '$lib/components/StrategySelect.svelte'
	import { Separator } from '$lib/components/ui/separator'
	import { getImageUrl } from '../../../../api'
	import { colorMap, selectedImage } from '../../../../stores'
	import type { Dataset, MetadataObject } from '../../../../types'

	import type { PageData } from './$types'

	export let data: PageData
	$: dataset = $page.params.dataset as Dataset

	$: ({ left, right } = data)

	$: selected_data = [
		left.find((item) => item.name == $selectedImage.split('.')[0]) as MetadataObject,
		right.find((item) => item.name == $selectedImage.split('.')[0]) as MetadataObject
	]
	$: src = getImageUrl($selectedImage, dataset, $page.params.runLeft, data.imageNames.left, false)
</script>

<MainLayout>
	<div slot="header">
		<Header>
			<div class="flex space-x-3">
				<ImageSelector {dataset} imageNames={data.imageNames.left} />
			</div>
		</Header>
	</div>

	<div slot="content" class="flex h-full space-x-3">
		{#key dataset}
			{#each { length: 2 } as _, i}
				<div class="h-full basis-1/3">
					<CompareColumn data={selected_data[i]} {src} column={i} />
				</div>
				<Separator orientation="vertical" />
			{/each}
			<div class="flex h-full basis-1/3 flex-col space-y-3">
				<div class="flex h-[400px] w-full items-center justify-center">
					<img {src} alt={$selectedImage} class="h-[400px] w-[400px] object-contain" />
				</div>
				<Separator />
				<div class="flex space-x-3">
					<ColorMapSelect />
					<Separator orientation="vertical" />
					<StrategySelect />
				</div>
				<Separator orientation="horizontal" />
				<div class="flex space-x-3">
					<DisplayOptions />
					<Separator orientation="vertical" />
					<SortingSelect />
				</div>
				<Separator />
			</div>
		{/key}
	</div>
</MainLayout>
