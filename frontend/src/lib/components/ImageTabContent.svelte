<script lang="ts">
	import { getImageUrl, getRelativePath } from '../../api'
	import { all_data, data, dataset, selected_params } from '../../stores'
	import { Separator } from './ui/separator'
	import { Label } from './ui/label'
	import Params from './Params.svelte'
	import MaskTable from './MaskTable.svelte'
	import MaskChart from './MaskChart.svelte'

	export let imageName = ''

	$: src = getImageUrl(imageName, $dataset)
</script>

{#await $data then d}
	<div class="flex h-full flex-row items-stretch space-x-3">
		<div class="flex basis-1/5 flex-col items-center space-y-3">
			<img {src} alt={imageName} class="h-60" />
			<Label>Original</Label>
			<Separator />
			<img src={getRelativePath(d ? d.annotated_image : '')} alt={'Annotated'} class="h-60" />
			<Label>Annotated</Label>
			<Separator />
			<Params />
		</div>
		<Separator orientation="vertical" />
		<div class="h-full basis-2/5 overflow-y-auto">
			<MaskTable />
		</div>
		<Separator orientation="vertical" />
		<div class="flex h-full basis-2/5 flex-col overflow-y-auto">
			<MaskChart />
			<Separator />
		</div>
	</div>
{/await}
