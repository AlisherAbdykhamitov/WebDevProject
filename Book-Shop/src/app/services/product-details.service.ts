import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {PRODUCTS} from '../data/products';
import {HttpClient,  HttpHeaders} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProductDetailsService {

  BASE_URL = 'http://127.0.0.1:8000'

  constructor(private http: HttpClient) { }

  getDetailsOfProduct(productId: number): Observable<any>{
    // return of(PRODUCTS.find(product => product.id === productId));
    return this.http.get(`${this.BASE_URL}/api/products/${productId}/`);

  }
}
