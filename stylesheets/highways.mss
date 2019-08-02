@color_transport: #000;
@color_transport_casing: #fff;

#roads {
  ::casing,
  ::outline,
  {
    line-cap: butt;
    line-width: 0;
    line-color: @color_transport_casing;
  }

  line-join: round;
  line-cap: round;
  line-width: 2;
  line-color: @color_transport;
}