<script lang="ts">
	import { selected_params, type Param } from '../../stores'
	import Label from './ui/label/label.svelte'
	import { Toggle } from './ui/toggle'

	export let params: Param
	export let id: string
	$: selected = $selected_params.includes(id)
</script>

<Toggle
	class="flex h-fit flex-col p-3"
	variant="outline"
	pressed={selected}
	onPressedChange={(pressed) =>
		selected_params.update((arr) => (pressed ? [...arr, id] : arr.filter((val) => val != id)))}
>
	{#each Object.entries(params) as [param, value]}
		<div class="flex w-full flex-row justify-between hover:text-inherit">
			<Label>{param}:</Label>
			<Label>{value}</Label>
		</div>
	{/each}
</Toggle>
