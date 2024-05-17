<script lang="ts">
	import { page } from '$app/stores'
	import { getRoute } from '../../api'
	import { dataset } from '../../stores'
	import * as Select from './ui/select'

	$: selected = { value: $dataset }

	$: dataset.set(selected.value)
</script>

<Select.Root bind:selected>
	<Select.Trigger class="w-[180px]">
		<Select.Value placeholder="Select dataset" />
	</Select.Trigger>
	<Select.Content>
		<a href={getRoute($page.params.run, $page.params.param, 'oxford_flowers102', $page.route.id)}>
			<Select.Item value="oxford_flowers102">oxford_flowers102</Select.Item>
		</a>
		<a href={getRoute($page.params.run, $page.params.param, 'imagenet2012', $page.route.id)}>
			<Select.Item value="imagenet2012">imagenet2012</Select.Item>
		</a>
		<a href={getRoute($page.params.run, $page.params.param, 'oxford_iiit_pet', $page.route.id)}>
			<Select.Item value="oxford_iiit_pet">oxford_iiit_pet</Select.Item>
		</a>
	</Select.Content>
</Select.Root>
