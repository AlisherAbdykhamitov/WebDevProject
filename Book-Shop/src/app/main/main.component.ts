import { Component, OnInit } from '@angular/core';
import {CategoriesService} from '../services/categories.service';
import {Category} from '../models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  categories: Category[] = [];
  constructor(private categoriesService: CategoriesService) { }

  ngOnInit(): void {
    this.getCompanyList();
  }
  getCompanyList() {
    this.categoriesService.getCategoryList()
      .subscribe(categories => {
        this.categories = categories
      });
  }

}
