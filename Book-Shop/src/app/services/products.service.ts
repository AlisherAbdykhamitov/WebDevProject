import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {PRODUCTS} from '../data/products';
import {HttpClient,  HttpHeaders} from '@angular/common/http';
// import {Product} from '../data/products';
import {Product} from '../models';


@Injectable({
  providedIn: 'root'
})
export class ProductsService {

  BASE_URL = 'http://127.0.0.1:8000'
  // private productsUrl = 'categories/:id/products'
  constructor(private http: HttpClient) { }

  getProducts(): Observable<Product[]>{
    // return this.http.get<Product[]>(this.productsUrl);
    return this.http.get<Product[]>(`${this.BASE_URL}/api/products`);

  }
  getProductsByCategories(Id: number): Observable<any>{
    return this.http.get<Product[]>(`${this.BASE_URL}/api/categories/:id/products`);
    // return of(PRODUCTS.filter(product => product.categoryId === Id));
  }
  deleteProduct(id): Observable<any> {
    return this.http.delete(`${this.BASE_URL}/api/products/${id}/`);
  }

}
