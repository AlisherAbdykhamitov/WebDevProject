import { Component, OnInit } from '@angular/core';
import {CategoriesService} from '../services/categories.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  categories = [];
  constructor(private categoriesService: CategoriesService) { }

  ngOnInit(): void {
    this.getCategories();
  }
  getCategories(): void{
    this.categoriesService.getCategories().subscribe(categories => this.categories = categories);
  }

}
