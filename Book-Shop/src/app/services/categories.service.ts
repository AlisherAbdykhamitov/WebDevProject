import { Injectable } from '@angular/core';
import {Categories} from '../data/categories';
import {Observable, of} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CategoriesService {

  constructor() { }
  getCategories(): Observable<any>{
    return of(Categories);
  }
}
