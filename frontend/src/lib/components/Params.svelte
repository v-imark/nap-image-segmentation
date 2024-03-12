<script lang="ts">
	import { EXAMPLE_PARAMS } from '../../api'
	import { selected_params } from '../../stores'
	import type { Param } from '../../types'
	import { Label } from './ui/label'

	$: params = EXAMPLE_PARAMS.find((val) => val.id == $selected_params) as Param
</script>

<div class="flex w-full flex-col space-y-1.5">
	{#each Object.entries(params) as [key, value]}
		<div class="flex flex-row justify-between">
			<Label>{key}</Label>
			<Label>{value}</Label>
		</div>
	{/each}
</div>
