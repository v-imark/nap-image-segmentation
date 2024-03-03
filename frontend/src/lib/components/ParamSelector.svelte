<script lang="ts">
	import { PARAM_IDS, SEG_PARAMS, selected_params } from '../../stores'
	import ParamToggle from './ParamToggle.svelte'
	import { Checkbox } from './ui/checkbox'
	import { Label } from './ui/label'

	$: checked = $selected_params.length == PARAM_IDS.length
</script>

<div class="flex flex-col space-y-3">
	<Label class="text-xl">Select Parameters</Label>
	<div class="flex items-center space-x-2">
		<Checkbox
			id="select-all"
			{checked}
			onCheckedChange={(c) => (c ? selected_params.set(PARAM_IDS) : selected_params.set([]))}
		/>
		<Label
			for="select-all"
			class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
		>
			All
		</Label>
	</div>
	{#each SEG_PARAMS as [id, params]}
		<ParamToggle {params} {id} />
	{/each}
	{$selected_params.toString()}
</div>
