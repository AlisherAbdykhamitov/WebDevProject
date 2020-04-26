import { Injectable } from '@angular/core';
// import {Categories} from '../data/categories';
import {Observable, of} from 'rxjs';
import {HttpClient} from "@angular/common/http";
import {Category, LoginResponse} from '../models';

@Injectable({
  providedIn: 'root'
})
export class CategoriesService {

  // constructor() { }
  // getCategories(): Observable<any>{
  //   return of(Categories);
  // }
  BASE_URL = 'http://127.0.0.1:8000'

  constructor(private http: HttpClient) {}

  getCategoryList(): Observable<Category[]> {
    return this.http.get<Category[]>(`${this.BASE_URL}/api/categories/`);
  }
              
  getCategory(id): Observable<Category> {
    return this.http.get<Category>(`${this.BASE_URL}/api/categories/${id}/`);
  }

  deleteCategory(id): Observable<any> {
    return this.http.delete(`${this.BASE_URL}/api/categories/${id}/`);
  }

  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.BASE_URL}/api/login/`, {
      username,
      password
    })
  }

  
 
}
