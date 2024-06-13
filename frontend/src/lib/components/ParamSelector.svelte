<script lang="ts">
	import * as Select from './ui/select'
	import { getRoute } from '../../api'
	import * as Tooltip from '$lib/components/ui/tooltip'
	import { page } from '$app/stores'
	import { Label } from './ui/label'
	import { ParamKeys } from '../../types'
	export let column: number | undefined

	const keys = ['paramLeft', 'paramRight', 'param']
	$: key = column != undefined ? keys[column] : keys[2]
	let runs = Object.keys($page.data.params)
	$: selected = { value: $page.params[key] }
	$: selected.value = $page.params[key]

	const href = (col: number | undefined, run: string, paramId: string) => {
		if (col == 0) {
			return `/${$page.params.dataset}/${run}x${$page.params.runRight}/${paramId}x${$page.params.paramRight}`
		}
		if (col == 1) {
			return `/${$page.params.dataset}/${$page.params.runLeft}x${run}/${$page.params.paramLeft}x${paramId}`
		}
		return `/${run}/${paramId}/${$page.params.dataset}`
	}
</script>

<Select.Root selected={{ value: $page.params[key] }}>
	<Select.Trigger class="w-44">
		<div>{selected.value}</div>
	</Select.Trigger>
	<Select.Content class="flex flex-col">
		{#each runs as run}
			<Select.Group>
				<Select.Separator />
				<Select.Label>{run}</Select.Label>
				{#each $page.data.params[run] as param}
					<Tooltip.Root>
						<Tooltip.Trigger>
							<div class="w-[170px]">
								<a href={href(column, run, param.id)}>
									<Select.Item value={param.id}></Select.Item>
								</a>
							</div>
						</Tooltip.Trigger>
						<Tooltip.Content strategy="fixed">
							<Label>{param.id}</Label>
							{#each ParamKeys as paramkey}
								<p>{paramkey}: {param[paramkey]}</p>
							{/each}
						</Tooltip.Content>
					</Tooltip.Root>
				{/each}
			</Select.Group>
		{/each}
	</Select.Content>
</Select.Root>
