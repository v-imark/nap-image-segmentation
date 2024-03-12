<script lang="ts">
	import * as Select from './ui/select'
	import { dataset } from '../../stores'

	$: selected = { value: $dataset }

	$: dataset.set(selected.value)
</script>

<Select.Root bind:selected>
	<Select.Trigger class="w-[180px]">
		<Select.Value placeholder="Select dataset" />
	</Select.Trigger>
	<Select.Content>
		<Select.Item value="oxford_flowers102">oxford_flowers102</Select.Item>
		<Select.Item value="imagenet2012">imagenet2012</Select.Item>
	</Select.Content>
</Select.Root>
