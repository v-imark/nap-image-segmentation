<script lang="ts">
	import { page } from '$app/stores'
	import Header from '$lib/components/Header.svelte'
	import MainLayout from '$lib/components/MainLayout.svelte'
	import { type Dataset, type Param } from '../../../../types'
	import type { PageData } from './$types'
	import AnnotatedImage from '$lib/components/AnnotatedImage.svelte'
	import ParamSliders from '$lib/components/ParamSliders.svelte'
	import { Separator } from '$lib/components/ui/separator'
	import ParamSelector from '$lib/components/ParamSelector.svelte'
	import ImageMultiSelector from '$lib/components/ImageMultiSelector.svelte'
	import { getImageUrl } from '../../../../api'
	import { selectedImages } from '../../../../stores'
	import ColorMapSelect from '$lib/components/ColorMapSelect.svelte'
	import DisplayOptions from '$lib/components/DisplayOptions.svelte'
	import SortingSelect from '$lib/components/SortingSelect.svelte'
	import StrategySelect from '$lib/components/StrategySelect.svelte'
	export let data: PageData

	$: dataset = $page.params.dataset as Dataset
	$: metadata = data.metadata
	$: images = data.imageNames[dataset]
	$: $selectedImages = [images[0], images[1], images[2], images[3], images[4], images[5]]

	let params = {
		sam_params: data.params[$page.params.run][0],
		filters: { min_area: 0, iou_thresh: 1 }
	}
	$: console.log(data.params[$page.params.run])
	$: params.sam_params = data.params[$page.params.run].find(
		(item) => item.id == $page.params.param
	) as Param
	$: selectedDatas = metadata.filter((item) =>
		$selectedImages.find((name) => item.name == name.split('.')[0])
	)

	const getGrid = (length: number) => {
		if (length < 7) {
			return { size: 360, cols: 3 }
		}

		return { size: 280, cols: 4 }
	}
	$: grid = getGrid(selectedDatas.length)
</script>

<MainLayout>
	<div slot="header">
		<Header>
			<ImageMultiSelector imageNames={images} {dataset} />
		</Header>
	</div>
	<div slot="content" class="flex h-full space-x-3">
		<div class="grid h-full basis-3/4 grid-cols-{grid.cols}  place-items-center gap-4">
			{#key dataset}
				{#each selectedDatas as dataObj, i}
					<AnnotatedImage
						data={dataObj}
						{params}
						size={grid.size}
						src={getImageUrl(dataObj.name, dataset, $page.params.run, $selectedImages, true)}
					/>
				{/each}
			{/key}
		</div>
		<Separator orientation="vertical" />
		<div class="flex basis-1/4 flex-col space-y-3">
			<ParamSelector column={undefined} />
			{#key $page.params.param}
				<ParamSliders bind:params column={undefined} />
			{/key}
			<Separator />
			<div class="flex space-x-3">
				<ColorMapSelect />
				<Separator orientation="vertical" />
				<StrategySelect />
			</div>
			<Separator />
			<div class="flex space-x-3">
				<DisplayOptions />
				<Separator orientation="vertical" />
				<SortingSelect />
			</div>
			<Separator />
		</div>
	</div>
</MainLayout>
