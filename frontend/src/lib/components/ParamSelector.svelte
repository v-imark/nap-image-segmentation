<script lang="ts">
	import * as Select from './ui/select'
	import { selected_params } from '../../stores'
	import { PARAM_IDS } from '../../api'

	$: selected = { value: $selected_params }

	$: selected_params.set(selected.value)
</script>

<Select.Root bind:selected>
	<Select.Trigger class="w-[180px]">
		<Select.Value placeholder="Select params" />
	</Select.Trigger>
	<Select.Content>
		{#each PARAM_IDS as id}
			<Select.Item value={id}>{id}</Select.Item>
		{/each}
	</Select.Content>
</Select.Root>
