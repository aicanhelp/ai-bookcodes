package org.mds.experimental;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import lombok.experimental.Accessors;

@Getter
@Setter
@Accessors(chain = true)
@ToString
public class Data {
    private String name;
    private float runingTime;
    private float rating;
    private String title;
}
