import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {PRODUCTS} from '../data/products';
import {HttpClient,  HttpHeaders} from '@angular/common/http';
import {Product} from '../data/products';

@Injectable({
  providedIn: 'root'
})
export class ProductsService {

  private productsUrl = 'categories/:id/products'
  constructor(private http: HttpClient) { }

  getProducts(): Observable<Product[]>{
    return this.http.get<Product[]>(this.productsUrl);
  }

  getProductsByCategories(Id: number): Observable<any>{
    return of(PRODUCTS.filter(product => product.categoryId === Id));
  }


}
