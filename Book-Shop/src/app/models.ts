
export class Category {
    id: number;
    name: string;
    products: Product[]
  }
  
  export class LoginResponse {
    token: string;
  }

  export class Product {
    id: number;
    name: string;
    description: string;
    price:number;
  }