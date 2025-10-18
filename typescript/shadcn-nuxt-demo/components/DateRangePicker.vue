<script setup lang="ts">
import { ref } from 'vue'
import { RangeCalendar } from '@/components/ui/range-calendar'

const start = ref<Date>()
const end = ref<Date>()

const emit = defineEmits<{
  'update:start': [date: Date | undefined]
  'update:end': [date: Date | undefined]
}>()

const handleSelect = (range: { from: Date | undefined; to: Date | undefined }) => {
  start.value = range.from
  end.value = range.to
  emit('update:start', range.from)
  emit('update:end', range.to)
}
</script>

<template>
  <RangeCalendar
    v-model:start="start"
    v-model:end="end"
    @select="handleSelect"
  />
</template> 