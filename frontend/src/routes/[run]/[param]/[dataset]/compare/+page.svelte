<script lang="ts">
	import { page } from '$app/stores'
	import ColorInfo from '$lib/components/ColorInfo.svelte'
	import CompareColumn from '$lib/components/CompareColumn.svelte'
	import DisplayOptions from '$lib/components/DisplayOptions.svelte'
	import Header from '$lib/components/Header.svelte'
	import ImageSelector from '$lib/components/ImageSelector.svelte'
	import MainLayout from '$lib/components/MainLayout.svelte'
	import { Separator } from '$lib/components/ui/separator'
	import { getImageUrl } from '../../../../../api'
	import { type Dataset, type MetadataObject } from '../../../../../types'
	import type { PageData } from './$types'

	export let data: PageData
	$: dataset = $page.params.dataset as Dataset
	$: metadata = data[dataset]

	let selected_image = ''
	$: selected_data = metadata.find(
		(item) => item.name == selected_image.split('.')[0]
	) as MetadataObject
	$: src = getImageUrl(selected_image, dataset, $page.params.run, data.imageNames[dataset], false)
</script>

<MainLayout>
	<div slot="header">
		<Header>
			<div class="flex space-x-3">
				<ImageSelector {dataset} imageNames={data.imageNames} bind:image={selected_image} />
			</div>
		</Header>
	</div>
	<div slot="content" class="flex h-full space-x-3">
		{#each { length: 2 } as _, i}
			<div class="h-full basis-1/3">
				<CompareColumn data={selected_data} />
			</div>
			<Separator orientation="vertical" />
		{/each}
		<div class="flex h-full basis-1/3 flex-col space-y-3">
			<div class="flex h-[450px] w-full items-center justify-center">
				<img {src} alt={selected_image} class="h-[450px] w-[450px] object-contain" />
			</div>
			<Separator />
			<div class="flex space-x-3">
				<ColorInfo />
				<Separator orientation="vertical" />
				<DisplayOptions />
			</div>
		</div>
	</div>
</MainLayout>
