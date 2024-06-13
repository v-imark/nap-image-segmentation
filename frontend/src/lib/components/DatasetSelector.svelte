<script lang="ts">
	import { page } from '$app/stores'
	import * as Select from './ui/select'

	let selected = { value: $page.params.dataset }
</script>

<Select.Root bind:selected>
	<Select.Trigger class="w-[180px]">
		<Select.Value placeholder="Select dataset" />
	</Select.Trigger>
	<Select.Content>
		<a href={$page.url.href.replace(/imagenet2012|oxford_iiit_pet/gi, 'oxford_flowers102')}>
			<Select.Item value="oxford_flowers102">oxford_flowers102</Select.Item>
		</a>
		<a href={$page.url.href.replace(/oxford_flowers102|oxford_iiit_pet/gi, 'imagenet2012')}>
			<Select.Item value="imagenet2012">imagenet2012</Select.Item>
		</a>
		<a href={$page.url.href.replace(/imagenet2012|oxford_flowers102/gi, 'oxford_iiit_pet')}>
			<Select.Item value="oxford_iiit_pet">oxford_iiit_pet</Select.Item>
		</a>
	</Select.Content>
</Select.Root>
