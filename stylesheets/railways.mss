#railways {
  [kind='disused'] {
    ::line {
    line-width: 2.5;
    line-color: #d97c7c;
    }
  }
  [kind='used'] {
    ::line {
    line-width: 2.5;
    line-color: #d91a1a;
    }
  }
  ::dash {
    line-color: #fff;
    line-width: 1.75;
    line-dasharray: 6, 6;
  }
}
