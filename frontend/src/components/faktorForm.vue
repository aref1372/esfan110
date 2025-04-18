<template>
  <div class="max-w-md mx-auto p-4 bg-white rounded shadow">
    <h2 class="text-2xl font-bold mb-4">ثبت فاکتور خرید</h2>
    <form @submit.prevent="submitFaktor">
      <div class="mb-4">
        <label class="block">دسته‌بندی محصول:</label>
        <input v-model="kategoriName" class="border rounded w-full p-2" required />
      </div>

      <div class="mb-4">
        <label class="block">نام تامین‌کننده:</label>
        <input v-model="taminData.firmaN" class="border rounded w-full p-2" required />
      </div>

      <div class="mb-4">
        <label class="block">تلفن تامین‌کننده:</label>
        <input v-model="taminData.tel" class="border rounded w-full p-2" required />
      </div>

      <div class="mb-4">
        <label class="block">نام محصول:</label>
        <input v-model="produktData.name" class="border rounded w-full p-2" required />
      </div>

      <div class="mb-4">
        <label class="block">سایز محصول:</label>
        <input v-model="produktData.size" class="border rounded w-full p-2" required />
      </div>

      <div class="mb-4">
        <label class="block">تعداد:</label>
        <input v-model.number="faktorData.anzahl" type="number" class="border rounded w-full p-2" required />
      </div>

      <div class="mb-4">
        <label class="block">قیمت خرید به تومان:</label>
        <input v-model.number="faktorData.ghTomn" type="number" class="border rounded w-full p-2" required />
      </div>

      <div class="text-center">
        <button type="submit" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded">
          ثبت فاکتور
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { createFaktor } from '../services/faktorService.js'

const kategoriName = ref('')
const taminData = ref({ firmaN: '', tel: '' })
const produktData = ref({ name: '', size: '' })
const faktorData = ref({ anzahl: 0, ghTomn: 0 })

async function submitFaktor() {
  try {
    const kaufDatum = new Date().toISOString().split('T')[0]
    await createFaktor({
      kategori_name: kategoriName.value,
      tamink_data: taminData.value,
      produkt_data: produktData.value,
      faktor_data: faktorData.value,
      kauf_datum: kaufDatum,
    })
    alert('✅ فاکتور خرید با موفقیت ثبت شد!')
    resetForm()
  } catch (error) {
    console.error(error)
    alert('❌ خطا در ثبت فاکتور')
  }
}

function resetForm() {
  kategoriName.value = ''
  taminData.value = { firmaN: '', tel: '' }
  produktData.value = { name: '', size: '' }
  faktorData.value = { anzahl: 0, ghTomn: 0 }
}
</script>

<style scoped>
/* اگر دوست داشتی استایل بیشتر اضافه می‌کنیم */
</style>
