package org.mds.experimental;

import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.Test;

@Slf4j

class DataSourceTest {

    @Test
    public void testData() {
        new DataSource().data(10)
                .doOnNext(data -> {
                    data.forEach(data1 -> {
                        log.info(data1.toString());
                    });
                })
                .block();

    }
}