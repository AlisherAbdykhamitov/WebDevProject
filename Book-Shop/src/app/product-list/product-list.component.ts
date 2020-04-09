import { Component, OnInit } from '@angular/core';
import {ProductsService} from '../services/products.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {

  product = [];
  constructor(private productsService: ProductsService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getProductByCategories();
  }
  getProductByCategories(): void{
    const id = +this.route.snapshot.paramMap.get('id');
    this.productsService.getProductsByCategories(id).subscribe(res => this.product = res);
  }

}
