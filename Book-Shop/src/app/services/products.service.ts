import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {PRODUCTS} from '../data/products';

@Injectable({
  providedIn: 'root'
})
export class ProductsService {

  constructor() { }
  getProductsByCategories(Id: number): Observable<any>{
    return of(PRODUCTS.filter(product => product.categoryId === Id));
  }
}
