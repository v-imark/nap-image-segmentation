<script lang="ts">
	import { page } from '$app/stores'
	import Header from '$lib/components/Header.svelte'
	import MainLayout from '$lib/components/MainLayout.svelte'
	import { type Dataset } from '../../../../../types'
	import type { PageData } from './$types'
	import AnnotatedImage from '$lib/components/AnnotatedImage.svelte'
	import ParamSliders from '$lib/components/ParamSliders.svelte'
	import { Separator } from '$lib/components/ui/separator'
	export let data: PageData

	$: dataset = $page.params.dataset as Dataset
	$: metadata = data[dataset]

	let params = {
		sam_params: data.params[$page.params.run][0],
		filters: { min_area: 0, iou_thresh: 1 }
	}
</script>

<MainLayout>
	<div slot="header">
		<Header />
	</div>
	<div slot="content" class="flex h-full space-x-3">
		<div class="grid h-full basis-3/4 grid-cols-4 place-items-center gap-4">
			{#each { length: 12 } as _, i}
				<AnnotatedImage data={metadata[i]} {params} size={280} />
			{/each}
		</div>
		<Separator orientation="vertical" />
		<div class="h-full basis-1/4">
			{#key $page.params.param}
				<ParamSliders bind:params />
			{/key}
		</div>
	</div>
</MainLayout>
