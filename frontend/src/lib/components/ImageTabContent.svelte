<script lang="ts">
	import { toggleTable } from '../../stores'
	import { Separator } from './ui/separator'
	import MaskTable from './MaskTable.svelte'
	import MaskGrid from './MaskGrid.svelte'
	import AnnotatedWithSliders from './AnnotatedWithSliders.svelte'
	import type { Dataset, MetadataObject } from '../../types'

	export let data: MetadataObject[]
	export let dataset: Dataset
	let metaData1 = data[0]
	let metaData2 = data[1]
	let metaData3 = data[2]
</script>

<div class="flex h-full flex-row items-stretch space-x-3">
	<div class="flex h-full basis-4/12 flex-col">
		<div class="basis-1/4 pb-3">
			<AnnotatedWithSliders {dataset} {data} bind:selectedMetaData={metaData1} />
		</div>
		<Separator />
		<div class="basis-3/4 overflow-y-auto">
			{#if $toggleTable}
				<MaskTable data={metaData1} />
			{:else}
				<MaskGrid metaData={metaData1} />
			{/if}
		</div>
	</div>
	<Separator orientation="vertical" />
	<div class="flex h-full basis-4/12 flex-col">
		<div class="basis-1/4 pb-3">
			<AnnotatedWithSliders {dataset} {data} bind:selectedMetaData={metaData2} />
		</div>
		<Separator />
		<div class="basis-3/4 overflow-y-auto">
			{#if $toggleTable}
				<MaskTable data={metaData2} />
			{:else}
				<MaskGrid metaData={metaData2} />
			{/if}
		</div>
	</div>
	<Separator orientation="vertical" />
	<div class="flex h-full basis-4/12 flex-col">
		<div class="basis-1/4 pb-3">
			<AnnotatedWithSliders {dataset} {data} bind:selectedMetaData={metaData3} />
		</div>
		<Separator />
		<div class="basis-3/4 overflow-y-auto">
			{#if $toggleTable}
				<MaskTable data={metaData3} />
			{:else}
				<MaskGrid metaData={metaData3} />
			{/if}
		</div>
	</div>
</div>
