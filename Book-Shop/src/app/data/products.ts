export const PRODUCTS = [
  {
    categoryId: 1,
    id: 11,
    name: 'Джонатан Свифт «Путешествия Гулливера',
    price: '100$',
    image: 'https://cv4.litres.ru/pub/c/elektronnaya-kniga/cover_415/5311241-dzhonatan-svift-puteshestviya-lemuelya-gullivera.jpg',
    description: ''
  },
  {
    categoryId: 1,
    id: 12,
    name: 'Последний оракул',
    price: '100$',
    image: 'https://cv8.litres.ru/pub/c/elektronnaya-kniga/cover_415/330682-dzheyms-rollins-posledniy-orakul.jpg',
    description: ''
  },
  {
    categoryId: 1,
    id: 13,
    name: 'Зеленая Миля',
    price: '100$',
    image: 'https://cv5.litres.ru/pub/c/elektronnaya-kniga/cover_415/119255-stiven-king-zelenaya-milya-119255.jpg',
    description: ''
  },
  {
    categoryId: 1,
    id: 14,
    name: 'Артемис Фаул. Парадокс времени',
    price: '100$',
    image: 'https://cv3.litres.ru/pub/c/elektronnaya-kniga/cover_415/7528730-yon-kolfer-artemis-faul-paradoks-vremeni.jpg',
    description: ''
  },
  {
    categoryId: 1,
    id: 15,
    name: 'Владыка Марса',
    price: '100$',
    image: 'https://cv4.litres.ru/pub/c/elektronnaya-kniga/cover_415/125545-edgar-berrouz-vladyka-marsa.jpg',
    description: ''
  },
];

export interface Product{
  id:number,
  categoryId: number,
  url:string,
  name:string,
  image:string,
  description:string
} 
