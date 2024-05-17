<script lang="ts">
	import * as Select from './ui/select'
	import { getRoute } from '../../api'
	import { page } from '$app/stores'

	let runs = Object.keys($page.data.params)
	$: selected = { value: 'pps-32' }
</script>

<Select.Root bind:selected>
	<Select.Trigger class="w-[180px]">
		<Select.Value placeholder="Select params" />
	</Select.Trigger>
	<Select.Content>
		{#each runs as run}
			<Select.Group>
				<Select.Separator />
				<Select.Label>{run}</Select.Label>
				{#each $page.data.params[run] as param}
					<a href={getRoute(run, param.id, $page.params.dataset, $page.route.id)}>
						<Select.Item value={param.id} label={param.id}></Select.Item>
					</a>
				{/each}
			</Select.Group>
		{/each}
	</Select.Content>
</Select.Root>
