@building-fill: #555555;
@building-line: darken(@building-fill, 15%);

@building-major-fill: darken(@building-fill, 10%);
@building-major-line: darken(@building-major-fill, 15%);

#buildings {
  [zoom >= 14] {
    polygon-clip: false;
    polygon-fill: @building-fill;
    line-color: @building-line;
    line-width: .75;
    line-clip: false;
  }

  [amenity = 'place_of_worship'],
  [aeroway = 'terminal'],
  [aerialway = 'station'],
  [building = 'train_station'] {
    polygon-fill: @building-major-fill;
    line-color: @building-major-line;
  }
}
