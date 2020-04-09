import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {PRODUCTS} from '../data/products';

@Injectable({
  providedIn: 'root'
})
export class ProductDetailsService {

  constructor() { }

  getDetailsOfProduct(productId: number): Observable<any>{
    return of(PRODUCTS.find(product => product.id === productId));
  }
}
